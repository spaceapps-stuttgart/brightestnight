#include <stdio.h>
#include <sys/stat.h>
#include <stdlib.h>

void main(int argc, char *argv[]){
    char *name = argv[1];
    FILE *file;
    char *buffer;
    unsigned long fileLen;
    int imageWidth, imageHeight;

   if (argc !=4) {
	fprintf(stderr, "Usage: %s <pathname> <imageWidth> <imageHeight>\n", argv[0]);
	exit(EXIT_FAILURE);
   }     

   if ((imageWidth = atoi(argv[2])) && (imageHeight = atoi(argv[3]) <0)) {
	perror("width or height wrong! You are made of stupid!");
	exit(EXIT_FAILURE);
   } 
 

    
    //Open file
    file = fopen(name, "rb");
    if (!file)
    {
        fprintf(stderr, "Unable to open file %s", name);
        return;
    }

    //Get file length
    fseek(file, 0, SEEK_END);
    fileLen=ftell(file);
    fseek(file, 0, SEEK_SET);

    //Allocate memory
    buffer=(char *)malloc(fileLen+1);
    if (!buffer)
    {
        fprintf(stderr, "Memory error!");
                                fclose(file);
        return;
    }

    //Read file contents into buffer
    fread(buffer, fileLen, 1, file);
    fclose(file);

    //Do what ever with buffer
    printf("%x", (unsigned char)buffer[fileLen -1]);
//	printf("%x", (unsigned char)buffer[1]);


    free(buffer);
   // return 0;
}
