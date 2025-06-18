#include	<stdio.h>
#include	<stdlib.h>
#include	<string.h>
#include	<math.h>

#include	<sndfile.h>

#define		BUFFER_LEN	1024
#define		MAX_CHANNELS	6

static void process_data(double *data, int count, int channels);

int main (void) {
    SNDFILE	*infile, *outfile;
	SF_INFO 		sfinfo ;
	int			readcount, total_read;
	static double data [BUFFER_LEN] ;
	int format, major_count, subtype_count, m, s ;
	//const char *infilename = "./out2.mp3";
	const char *infilename = "/home/acid454/YDrive/workspace/yogaws/static-res/sounds/common10.mp3";
	const char *outfilename = "output.wav";


	memset (&sfinfo, 0, sizeof (sfinfo)) ;
	printf ("Version : %s\n\n", sf_version_string ()) ;

    if ((infile = sf_open(infilename, SFM_READ, &sfinfo)) == NULL)
	{
        printf ("Not able to open input file %s.\n", infilename) ;
		puts (sf_strerror (NULL)) ;
		sf_close (infile);
        return 0;
    }

    printf ("# Converted from file %s.\n", infilename) ;
	printf ("# Channels %d, Sample rate %d\n", sfinfo.channels, sfinfo.samplerate) ;
	printf ("# Frames %d, seekable %d\n", sfinfo.frames, sfinfo.seekable) ;
	printf ("# Format: 0x%X\n", sfinfo.format) ;



	/* Open the output file. */
	if (! (outfile = sf_open( outfilename, SFM_WRITE, &sfinfo ))) {
		printf ("Not able to open output file %s.\n", outfilename) ;
		puts (sf_strerror (NULL)) ;
		sf_close (infile) ;
		return 1 ;
	}


	total_read = 0;
	while ((readcount = (int)sf_read_double(infile, data, BUFFER_LEN))) {
		process_data (data, readcount, sfinfo.channels) ;
		sf_write_double (outfile, data, readcount) ;
		total_read += readcount;
	}
	printf("Total read %d doubles\n", total_read);

    sf_close (infile);
	sf_close (outfile);

	return 0 ;
}

static void process_data (double *data, int count, int channels) {
	double channel_gain [MAX_CHANNELS] = { 0.5, 0.8, 0.1, 0.4, 0.4, 0.9 } ;
	int k, chan ;

	/* Process the data here.
	** If the soundfile contains more then 1 channel you need to take care of
	** the data interleaving yourself.
	** Current we just apply a channel dependent gain.
	*/

	for (chan = 0; chan < channels; chan ++)
		for (k = chan; k < count; k += channels)
			data [k] *= channel_gain [chan] ;

	return ;
} /* process_data */
