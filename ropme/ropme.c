/*
gcc -static -fno-stack-protector -Wno-format-security ropme.c -o ropme
*/
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int do_something_usefull() {
  printf("Doing something useful ...");
  return(1);
}

void read_config() {
  char config[32];
  int i;
  FILE * pFile;
  //printf("%d\n", (int)getpid());
  pFile = fopen ("config.ini","rb");
  fgets (config,1024,pFile);
  printf("%s", config);
  printf("\n");
}


int main(int argc, char **argv) {
  //sleep(10);
  read_config();
  do_something_usefull();
  return(0);
}
