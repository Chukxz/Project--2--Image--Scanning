#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h>
#include <string.h>
#include "./test.h"
#include "./testing.h"
#include "unistd.h"


int createDatabase(int width, int height,char * mod_file_location1,char * buf){

    sqlite3 * db;
    char *err_msg = 0;
    int rc;
    rc = sqlite3_open("Pixel.db", &db);
    int * contain = malloc(100);

    if (rc != SQLITE_OK){
        fprintf(stderr,"Can't open database: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
        return 1;
    }

    for (int i = 0; i<height; i++){

        char name[30] = "Image_row_";
        char name_end[10];
        snprintf(name_end,sizeof(name_end),"%d",i+1);
        strncat(name,name_end,sizeof(name) - strlen(name) - 1);
        char* my_table = name;

        //Construct the SQL command to create the table
        char* sql_create =  malloc(strlen(my_table) + 50 + 25 * 4);
        sprintf(sql_create, "CREATE TABLE %s (id INTEGER PRIMARY KEY, ", my_table);

        char col_name_R[15] = "value_";
        char col_name_G[15] = "value_";
        char col_name_B[15] = "value_";
        char col_name_Gray[15] = "value_";

        char col_name_end_R[5];
        char col_name_end_G[5];
        char col_name_end_B[5];
        char col_name_end_Gray[5];

        snprintf(col_name_end_R,sizeof(col_name_end_R),"%s","R");
        strncat(col_name_R,col_name_end_R,sizeof(col_name_R) - strlen(col_name_R) - 1);
        char * my_col_R = col_name_R;

        snprintf(col_name_end_G,sizeof(col_name_end_G),"%s","G");
        strncat(col_name_G,col_name_end_G,sizeof(col_name_G) - strlen(col_name_G) - 1);
        char * my_col_G = col_name_G;

        snprintf(col_name_end_B,sizeof(col_name_end_B),"%s","B");
        strncat(col_name_B,col_name_end_B,sizeof(col_name_B) - strlen(col_name_B) - 1);
        char * my_col_B = col_name_B;

        snprintf(col_name_end_Gray,sizeof(col_name_end_Gray),"%s","Gray");
        strncat(col_name_Gray,col_name_end_Gray,sizeof(col_name_Gray) - strlen(col_name_Gray) - 1);
        char * my_col_Gray = col_name_Gray;
        
        strcat(sql_create, my_col_R);
        strcat(sql_create," TEXT, ");

        strcat(sql_create, my_col_G);
        strcat(sql_create," TEXT, ");

        strcat(sql_create, my_col_B);
        strcat(sql_create," TEXT, ");

        strcat(sql_create, my_col_Gray);
        strcat(sql_create," TEXT");

        strcat(sql_create, ");");

        //Execute the SQL command to create the table
        rc = sqlite3_exec(db,sql_create,0,0,&err_msg);

        if (rc != SQLITE_OK) {
            fprintf(stderr,"Failed to create table: %s\n", sqlite3_errmsg(db));
            sqlite3_free(err_msg);
            sqlite3_close(db);
            free(sql_create);
            return 1;
        }

        
        char * sql_insert = malloc(strlen(my_table) + 30 + 150 * width);
        for (int i = 0; i < width; i++){

            char stores[100];
            snprintf(stores,sizeof(stores),"%s", (_return_line_value_(1000,mod_file_location1,buf)));
            contain = getValues(4,mod_file_location1,buf,contain,stores);

            sprintf(sql_insert, "INSERT INTO %s (id",my_table);
            
            strcat(sql_insert,", ");
            strcat(sql_insert,my_col_R);
            strcat(sql_insert,", ");
            strcat(sql_insert, my_col_G);
            strcat(sql_insert,", ");
            strcat(sql_insert,my_col_B);
            strcat(sql_insert,", ");
            strcat(sql_insert, my_col_Gray);

            strcat(sql_insert, ") VALUES (");
            char id_index[10];
            sprintf(id_index,"%i",i+1);
            strcat(sql_insert,id_index);
            for (int j = 0; j < 4; j++){
                char contain_str[10];
                if(j==3){
                    contain[3] = (contain[1] + contain[2] + contain[3])/3;
                        sprintf(contain_str,"%i",contain[i]);
                        strcat(sql_insert,", '");
                        strcat(sql_insert,contain_str);
                        strcat(sql_insert,"'");
                }
                
                else{
                    sprintf(contain_str,"%i",contain[i]);
                    strcat(sql_insert,", '");
                    strcat(sql_insert,contain_str);
                    strcat(sql_insert,"', ");
                }
            }
            strcat(sql_insert, ");");
        }

        //Execute the sql command to insert the row
        rc = sqlite3_exec(db, sql_insert, 0, 0, &err_msg);
        if(rc != SQLITE_OK) {
            fprintf(stderr, "Failed to insert row: %s\n",sqlite3_errmsg(db));
            sqlite3_free(err_msg);
            sqlite3_close(db);
            free(sql_create);
            free(sql_insert);
            return 1;        
        }


        // Query table
        // char *query = "SELECT * FROM %s";
        // char *formatted_query = malloc(snprintf(NULL,0,query,my_table)+1);
        // sprintf(formatted_query,query,my_table);

        // rc = sqlite3_exec(db,formatted_query,0,0,&err_msg);

        // if (rc != SQLITE_OK){
        //     fprintf(stderr,"Failed to execute query: %s\n", sqlite3_errmsg(db));
        //     sqlite3_free(err_msg);
        // }
        
        // free(formatted_query);

            //Construct the SQL command to insert the rows
        
        
        sqlite3_free(err_msg);
        free(sql_create);
        free(sql_insert);
        free(contain);
    }

    sqlite3_close(db);

    printf("width of image is %d and height of image is %d",width,height);

    return 0;
}

int main(int argc, char * argv[]){

    char * buf = malloc(100);
    char file_location1[1024];
    char file_location2[1024];
    char mod_file_location1[1024];
    char mod_file_location2[1024];
    char buffer1[100];
    char buffer2[100];

    FILE * fptr = fopen("lookup.txt","r");

    if(fptr == NULL){
        printf("Error opening file!");
        // Program exits if the file pointer returns NULL.
        return -1;
    }

    for(int i=1; i<=1; i++){
        fgets(file_location1,1024,fptr);
    }

    for(int i=1; i<=2; i++){
        fgets(file_location2,100,fptr);
    }
    fclose(fptr);

    snprintf(mod_file_location1,strlen(file_location1),"%s",file_location1);
    snprintf(mod_file_location2,strlen(file_location2),"%s",file_location2);

    snprintf(buffer1,sizeof(buffer1),"%s", (_return_line_value_(1,mod_file_location1,buf)));    
    snprintf(buffer2,sizeof(buffer2),"%s", (_return_line_value_(2,mod_file_location1,buf)));

    int buffer1_int = (int) strtol(buffer1,NULL,10);

    int buffer2_int = (int) strtol(buffer2,NULL,10);

    printf("%d + %d = %d\n",buffer1_int,buffer2_int,buffer1_int+buffer2_int);

    
    char s[100];

    printf("%s\n",getcwd(s, 100));

    chdir(mod_file_location2);

    printf("%s\n",getcwd(s, 100));

    createDatabase(buffer1_int,buffer2_int,mod_file_location1,buf);

    free(buf);

    chdir("../../../");

    printf("%s\n",getcwd(s, 100));
}