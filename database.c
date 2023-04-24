#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h>
#include <string.h>

int createDatabase(int width, int height){
    
    sqlite3 * db;
    char *err_msg = 0;
    int rc;
    rc = sqlite3_open("Pixel.db", &db);

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
        char* sql_create = malloc(strlen(my_table) + 50 + 25 * 4);
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
            sprintf(sql_insert, "INSERT INTO %s (id, ",my_table);
            
            strcat(sql_insert,", ");
            strcat(sql_insert,my_col_R);
            strcat(sql_insert,", ");
            strcat(sql_insert, my_col_G);
            strcat(sql_insert,", ");
            strcat(sql_insert,my_col_B);
            strcat(sql_insert,", ");
            strcat(sql_insert, my_col_Gray);

            strcat(sql_insert,(") VALUES (%d", i + 1));//More work to be done here on the values
            for (int j = 0; j < 4; j++){
                char col_value[20];

                strcat(sql_insert,", '");
                strcat(sql_insert, col_value);
                strcat(sql_insert,"'");
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
        
        free(name);
        free(name_end);
        free(col_name_R);
        free(col_name_G);
        free(col_name_B);
        free(col_name_Gray);
        free(col_name_end_R);
        free(col_name_end_G);
        free(col_name_end_B);
        free(col_name_end_Gray);
        free(my_col_R);
        free(my_col_G);
        free(my_col_B);
        free(my_col_Gray);
        free(my_table);
        free(sql_create);
        free(sql_insert);
        free(err_msg);
    }

    sqlite3_close(db);

    printf("width of image is %d and height of image is %d",width,height);

    return 0;
}

int main(int argc, char * argv[]){
    
    char *filename1 = "./store1.txt";
    char *filename2 = "./store2.txt";

    FILE * fptr1 = fopen(filename1,"r");

    if(fptr1 == NULL){
        printf("Error opening file!");
        // Program exits if the file pointer returns NULL.
        return -1;
    }

    fseek(fptr1,0,SEEK_END);
    long size1 = ftell(fptr1);
    fseek(fptr1,0,SEEK_SET);

    char * buffer1 = malloc(size1);

    fread(buffer1,1,size1,fptr1);

    fclose(fptr1);

    FILE * fptr2 = fopen(filename2,"r");

    if(fptr2 == NULL){
        printf("Error opening file!");
        // Program exits if the file pointer returns NULL.
        return -1;
    }

    fseek(fptr2,0,SEEK_END);
    long size2 = ftell(fptr2);
    fseek(fptr2,0,SEEK_SET);

    char * buffer2 = malloc(size2);

    fread(buffer2,1,size2,fptr2);

    fclose(fptr2);

    int buffer1_int = (int) strtol(buffer1,NULL,10);

    int buffer2_int = (int) strtol(buffer2,NULL,10);

    printf("%d + %d = %d\n",buffer1_int,buffer2_int,buffer1_int+buffer2_int);

    createDatabase(buffer1_int,buffer2_int);
}