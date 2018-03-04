/*
 * Sidharth Bambah
 * UID: 904 787 435
 * */

#include <stdio.h>
#include <stdlib.h>

#define SPACE ' '

int frobcmp(char const* a, char const* b){
	for(;; a++, b++){
		if(*a == SPACE && *b == SPACE) {return 0;}
		else if (*a == SPACE || ((*a^42) < (*b^42))) {return -1;}
		else if (*b == SPACE || ((*a^42) > (*b^42))) {return 1;}	
	}	
}

int cmp(const void* input1, const void* input2){
	const char* a = *(const char**)input1;
	const char* b = *(const char**)input2;
	return frobcmp(a,b);
}

void inputError(){
	if(ferror(stdin)){
		fprintf(stderr, "Error during file reading");
		exit(1);
	}
}
int main(void){
	char* word;
	char** words;
	word = (char*)malloc(sizeof(char));
	words = (char**)malloc(sizeof(char*));
	char current = getchar();
	inputError();
	char next = getchar();
	inputError();
	int letterCounter = 0;
	int wordCounter = 0;
	while(current != EOF && !ferror(stdin)){
		word[letterCounter] = current;
		char* extra = realloc(word, (letterCounter+2)*sizeof(char));
		if(extra != NULL){
			word = extra;
		}
		else{
			free(word);
			fprintf(stderr, "Memory Allocation Error");
			exit(1);
		}
		if(current == SPACE){
			words[wordCounter] = word;
			char** anotherList = realloc(words, (wordCounter+2)*sizeof(char*));
			if(anotherList != NULL){
				words = anotherList;
				wordCounter++;
				word = NULL;
				word = (char*)malloc(sizeof(char));
				letterCounter = -1;	
			}
			else{
				free(words);
				fprintf(stderr, "Memory Allocation Error");
				exit(1);
			}
		}
		if(next == EOF && current == SPACE){
			break;
		}
		else if(current == SPACE && next == SPACE){
			while(current == SPACE){
				current = getchar();
				inputError();
			}
			next = getchar();
			inputError();
			letterCounter++;
			continue;
		}
		else if(next == EOF){
			current = SPACE;
			letterCounter++;
			continue;
		}
		current = next;
		next = getchar();
		inputError();
		letterCounter++;
	}
	qsort(words, wordCounter, sizeof(char*), cmp);
	int i;
	for(i = 0; i < wordCounter; i++){
		int j;
		for(j = 0; ; j++){
			if(putchar(words[i][j]) == EOF){
				fprintf(stderr, "Error during character writing");
				exit(1);
			}
			if(words[i][j] == SPACE){
				break;
			}
		}
	}
	for(i = 0; i < wordCounter; i++){
		free(words[i]);
	}
	free(words);
	exit(0);
}
