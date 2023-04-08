if __name__ != "__main__":
    import re
    def tupletolist(tuple):
        """
        Custom function for converting tuple to string and then
        splitting it to a list of substrings that are 
        seperated by parenthesis '(' or ')' and commas with spaces
        ', ' which are then returned. The return list can further be
        indexed to get the string item and convert it to an integer
        if desired.
        """
        tuple_string = str(tuple)
        tuple_string_list = re.split('[\(]|[, ]|[\)]',tuple_string)
        return tuple_string_list