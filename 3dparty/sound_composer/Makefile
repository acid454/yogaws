ROOT_DIR := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))
LIBSNDFILE := libsndfile-1.2.2
PROJECT_NAME := sound_composer

all:
	g++ -I${ROOT_DIR}/${LIBSNDFILE}/include  -o ${ROOT_DIR}/${PROJECT_NAME} ${ROOT_DIR}/main.cpp \
		${ROOT_DIR}/${LIBSNDFILE}/src/.libs/libsndfile.a /usr/lib/x86_64-linux-gnu/libmp3lame.a -lm -lmpg123

install:
	cp ${ROOT_DIR}/${PROJECT_NAME} ${ROOT_DIR}/../../scripts

sndfile:
	[ ! -d ${ROOT_DIR}/${LIBSNDFILE} ] && { \
		rm -rf ${ROOT_DIR}/${LIBSNDFILE} && \
		rm -rf ${ROOT_DIR}/${LIBSNDFILE}.tar.gz && \
		wget https://github.com/libsndfile/libsndfile/archive/refs/tags/1.2.2.tar.gz -O ${ROOT_DIR}/${LIBSNDFILE}.tar.gz && \
		tar -xvf ${ROOT_DIR}/${LIBSNDFILE}.tar.gz -C ${ROOT_DIR}; \
	} || true
	make -C ${ROOT_DIR}/${LIBSNDFILE} distclean || true
	cd ${ROOT_DIR}/${LIBSNDFILE} && autoreconf -vif && ./configure --enable-werror --enable-static=yes --enable-shared=no --disable-external-libs && make
