#include <stdio.h>
#include <sys/stat.h>
#include <stdlib.h>
void main(){
        char *name ="Image_bgr.raw";
    FILE *file;
    char *buffer;
    unsigned long fileLen;

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
}
