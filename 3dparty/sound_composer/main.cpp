/*
 * main.cpp
 *
 * Copyright 2025 Repnikov Dmitry <acid454@yoga7>
 * YogaWS sound composer. Takes csv lines with mp3/wav file names on input,
 *  and compose them as one output. Each line is a second.
 */

#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <sndfile.h>



#define		DEBUG if (0)
#define		YOGAWS_SAMPLE_RATE		44100

struct snd_file {
	SNDFILE *pSndFile;
	std::string name;
};

void split_table_line(std::string& s, std::vector<std::string>& v) {
	std::string token;
	size_t pos = 0;


	while ((pos = s.find(",")) != std::string::npos) {
		v.push_back(s.substr(0, pos));
		s.erase(0, ++pos);
	}
	v.push_back(s);
}

int main (void) {
	std::string table_line;
	std::vector<snd_file> sound_table;
	std::vector<std::string> sound_files;

    SNDFILE *outfile;
	SF_INFO out_sfinfo, tmp_sfinfo;
	int readcount, i;
	double out_data[YOGAWS_SAMPLE_RATE];
	double trc_data[YOGAWS_SAMPLE_RATE];


	/* Initialize output file */
	std::memset(&out_sfinfo, 0, sizeof(out_sfinfo));
	out_sfinfo.frames = 0;
	out_sfinfo.samplerate = YOGAWS_SAMPLE_RATE;
	out_sfinfo.channels = 1;
	out_sfinfo.format = SF_FORMAT_MPEG | SF_FORMAT_MPEG_LAYER_III;
#if 1
	if ((outfile = sf_open_fd(fileno(stdout), SFM_WRITE, &out_sfinfo, 0 )) == NULL)
#else
	if ((outfile = sf_open("output.mp3", SFM_WRITE, &out_sfinfo)) == NULL)
#endif
	{
		printf("Not able to open output file.\n");
		puts(sf_strerror (NULL));
		return 1;
	}

	

	/* Read stdin line by line, in format */
	/* track1-file-name.mp3, track2-file-name.mp3, -can-be-empty, track2-file-name.mp3 */
	/* ,,,change-track.mp3 */
	/* ...etc */
	while (!std::getline(std::cin, table_line).eof()) {
		DEBUG std::cerr << "--- line ok ---" << std::endl;

		sound_files.clear();
		split_table_line(table_line, sound_files);
		DEBUG std::cerr << "input vector length: " << sound_files.size() << std::endl;

		for (uint track_num = 0; track_num < sound_files.size(); track_num++) {
			DEBUG std::cerr << "check sound_table size: " << sound_table.size() << ", current index " << track_num << std::endl;

			if (sound_table.size() < track_num + 1)
				sound_table.push_back( { NULL, "" } );

			if (!sound_files[track_num].length())
				continue;	/* Empty track */

			/* Input track is not empty, (re)start it */
			snd_file *pCurTrack = &sound_table[track_num];
			if (pCurTrack->name != sound_files[track_num]) {
				if (pCurTrack->pSndFile != NULL)
					sf_close(pCurTrack->pSndFile);

				std::memset(&tmp_sfinfo, 0x00, sizeof(tmp_sfinfo));
				pCurTrack->name = sound_files[track_num];
				if ((pCurTrack->pSndFile = sf_open(pCurTrack->name.c_str(), SFM_READ, &tmp_sfinfo)) == NULL) {
					DEBUG std::cerr << "Unable to open track #" << track_num << ": " << pCurTrack->name << std::endl;
					pCurTrack->name = "";
				} else
					DEBUG std::cerr << "OK open track #" << track_num << ": " << pCurTrack->name << " - open" << std::endl;
			} else {
				sf_seek(pCurTrack->pSndFile, 0, SEEK_SET);
				DEBUG std::cerr << "OK open track #" << track_num << ": " << pCurTrack->name << " - rewind" << std::endl;
			}
		}


		/* Processing current second of flow */
		std::memset(out_data, 0x00, sizeof(out_data));
		for (snd_file& s : sound_table) {
			if (s.pSndFile == NULL)
				continue;

			DEBUG std::cerr << "-- compose file: " << s.name << std::endl;

			/* std::memset(trc_data, 0x00, sizeof(trc_data)); */
			readcount = (int)sf_read_double(s.pSndFile, trc_data, YOGAWS_SAMPLE_RATE);
			for (i = 0; i < readcount; i++)
				out_data[i] += trc_data[i];

			/*if (readcount < YOGAWS_SAMPLE_RATE) {
				std::cout << "Close track " << s.name << " - complete" << std::endl;
				sf_close(s.pSndFile);
				s.pSndFile = NULL;
				s.name  = "";
			} */
		}

		sf_write_double(outfile, out_data, YOGAWS_SAMPLE_RATE);
	}


	for (const snd_file& s : sound_table)
		if (s.pSndFile != NULL)
			sf_close(s.pSndFile);
	
	sf_close(outfile);
	return 0;
}
