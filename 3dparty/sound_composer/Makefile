ROOT_DIR := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))
OUTPUT_DIR := $(ROOT_DIR)/output
LIBSNDFILE := libsndfile-1.2.2
LIBSNDFILE_URL := "https://github.com/libsndfile/libsndfile/archive/refs/tags/1.2.2.tar.gz"
LIBSND_DIR := $(OUTPUT_DIR)/$(LIBSNDFILE)
PROJECT_NAME := sound_composer



all:
	@mkdir -p $(OUTPUT_DIR)
	g++ -I$(LIBSND_DIR)/include  -o $(OUTPUT_DIR)/$(PROJECT_NAME) $(ROOT_DIR)/main.cpp \
		$(LIBSND_DIR)/src/.libs/libsndfile.a /usr/lib/x86_64-linux-gnu/libmp3lame.a -lm -lmpg123

install:
	cp $(OUTPUT_DIR)/$(PROJECT_NAME) $(ROOT_DIR)/../../scripts

sndfile:
	[ ! -d $(LIBSND_DIR) ] && ( \
		$(MAKE) distclean && \
		wget $(LIBSNDFILE_URL) -O $(OUTPUT_DIR)/$(LIBSNDFILE).tar.gz && \
		tar -xvf $(OUTPUT_DIR)/$(LIBSNDFILE).tar.gz -C $(OUTPUT_DIR); \
	) || true

	@$(MAKE) -C $(LIBSND_DIR) distclean || true
	cd $(LIBSND_DIR) && autoreconf -vif && ./configure --enable-werror --enable-static=yes --enable-shared=no --disable-external-libs && $(MAKE)

distclean:
	rm -rf $(OUTPUT_DIR)/*