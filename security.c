//
//  security.c
//  
//
//  Created by Nguyen Trung Huan on 26/3/18.
//
#define BUFFER_LENGTH 100
#include <stdio.h>
int main()
{
    char guessedDateStr[BUFFER_LENGTH]; // to input string
    char guessedKeyStr[BUFFER_LENGTH]; // to input key
    int date;
    int key;
    // Preamble
    printf("I hope you are not an intruder...\n");
    printf("Carefully enter my special day...\n");
    printf("Hint: ZILLIONS of people showed up but the media fooled everyone otherwise\n");
    
    // Check date
    int isDateCorrect = 0;
    while (isDateCorrect == 0)
    {
        printf("\nmmddyyyy : ");
        scanf("%s", guessedDateStr);
        
        if (strcmp(guessedDateStr, "01202017") == 0)
        {
            printf("Good job. Onto the next step!");
            isDateCorrect = 1;
        }
        else
        {
            printf("It's a wrong date. Try harder\n");
        }
    }
    date = atoi(guessedDateStr);
    
    // Produce key based on the correct date
    key = (date << 2) ^ date;

    printf("\nNow key in the secret key... Do you remember our favorite operations?\n");
    
    int isKeyCorrect = 0;
    while (isKeyCorrect == 0)
    {
        printf("hex (starting with 0x) : ");
        scanf("%s", guessedKeyStr);
        
        int guessedKey = (int)strtol(guessedKeyStr, NULL, 16);
        
        if (key == guessedKey)
        {
            printf("Congratulations! The password is \"dear_putin\"\n");
            isKeyCorrect = 1;
        }
        else
        {
            printf("Oh no... You can key in the secret key again\n");
        }
    }
    
    return 0;
}
