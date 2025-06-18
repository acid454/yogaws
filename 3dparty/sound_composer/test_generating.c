#include	<stdio.h>
#include	<stdlib.h>
#include	<string.h>
#include	<math.h>

#include	<sndfile.h>

#define		BUFFER_LEN	1024
#define		WORKOUT_TIME_SECONDS	(30*60)
#define		YOGAWS_SAMPLE_RATE		44100
#define		COMMON_SOUND_START_TS	3

static void process_data(double *data, int count, int channels);



int main (void) {
    SNDFILE *tick_sfile, *common_sfile, *outfile;
	SF_INFO out_sfinfo, tmp_sfinfo;
	int	readcount, i, j, update_tick_data_buffer;
	double out_data[YOGAWS_SAMPLE_RATE];
	double common_data[YOGAWS_SAMPLE_RATE];

	int format, major_count, subtype_count, m, s ;
    const char *tick_file = "/home/acid454/YDrive/workspace/yogaws/static-res/wavs/tick1-44100.wav";
	const char *message_file = "/home/acid454/YDrive/workspace/yogaws/static-res/sounds/common10.mp3";
	const char *outfilename = "output.mp3" ;


	memset(&out_sfinfo, 0, sizeof(out_sfinfo));
	printf("SF version : %s\n\n", sf_version_string());

	/* Create output file */
	out_sfinfo.frames = 0; //WORKOUT_TIME_SECONDS * YOGAWS_SAMPLE_RATE;
	out_sfinfo.samplerate = YOGAWS_SAMPLE_RATE;
	out_sfinfo.channels = 1;
	out_sfinfo.format = SF_FORMAT_MPEG | SF_FORMAT_MPEG_LAYER_III;
	if ((outfile = sf_open(outfilename, SFM_WRITE, &out_sfinfo )) == NULL) {
		printf("Not able to open output file %s.\n", outfilename);
		puts(sf_strerror (NULL));
		return 1;
	}


	/* Open tick and common files */
	memset(&tmp_sfinfo, 0x00, sizeof(tmp_sfinfo));
    if ((tick_sfile = sf_open(tick_file, SFM_READ, &tmp_sfinfo)) == NULL) {
		printf ("Not able to open input file %s.\n", tick_file) ;
		puts (sf_strerror (NULL)) ;
		sf_close (outfile);
		return 1;
	}

	memset(&tmp_sfinfo, 0x00, sizeof(tmp_sfinfo));
    if ((common_sfile = sf_open(message_file, SFM_READ, &tmp_sfinfo)) == NULL) {
		printf ("Not able to open input file %s.\n", message_file) ;
		puts (sf_strerror (NULL)) ;
		sf_close (tick_sfile);
		sf_close (outfile);
		return 1;
	}


	/* Now processing every second */
	update_tick_data_buffer = 1;
	readcount = 1;
	for (i = 0; i < WORKOUT_TIME_SECONDS; i++) {
		if (update_tick_data_buffer) {
			memset(out_data, 0x00, sizeof(out_data));
			sf_seek(tick_sfile, 0, SEEK_SET);
			sf_read_double(tick_sfile, out_data, YOGAWS_SAMPLE_RATE);
			update_tick_data_buffer = 0;
		}

		if ((i >= COMMON_SOUND_START_TS) && (readcount > 0)) {
			if ((readcount = (int)sf_read_double(common_sfile, common_data, YOGAWS_SAMPLE_RATE)) > 0) {
				/* Merge tick and voice */
				for (j = 0; j < readcount; j++) {
					//printf("%f %f\n", out_data[j], common_data[j]);
					out_data[j] += common_data[j];
				}
				update_tick_data_buffer = 1;
			}
		}

		sf_write_double(outfile, out_data, YOGAWS_SAMPLE_RATE);
	}


    sf_close(tick_sfile);
	sf_close(common_sfile);
	sf_close(outfile);

	return 0 ;
}
