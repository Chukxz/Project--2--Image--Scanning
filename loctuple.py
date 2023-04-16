if __name__ != "__main__":
    import re
    def tupletolist(tuple):
        """
        Custom function for converting tuple to list
        """
        tuple_string = str(tuple)
        tuple_string_list = re.split(r'[\[]|[\(]|[, ]|[\)]|[\]]',tuple_string)
        return_list =  [int(j) for j in tuple_string_list if j!='']
        return return_list