import re
class Dekimashita:

    @staticmethod
    def vdict(data, chars):
        """
        Filter dictionary values recursively, ignoring specified characters.
        Double spaces are replaced with a single space.

        Args:
        data (dict or list): Data (dictionary or list containing dictionaries) to filter.
        chars (list): List of characters to filter.

        Returns:
        dict or list: Filtered data.
        """
        if isinstance(data, dict):
            clear_dict = {}
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    clear_dict[key] = Dekimashita.vdict(value, chars)

                elif isinstance(value, str):
                    clear_value = ''.join(char for char in value if char not in chars)
                    clear_value = ' '.join(clear_value.split())  # Remove double spaces
                    clear_dict[key] = clear_value

                else:
                    clear_dict[key] = value

            return clear_dict
        elif isinstance(data, list):
            clear_list = []
            for item in data:
                if isinstance(item, (dict, list)):
                    clear_list.append(Dekimashita.vdict(item, chars))

                elif isinstance(item, str):
                    clear_value = ''.join(char for char in item if char not in chars)
                    clear_value = ' '.join(clear_value.split())  # Remove double spaces
                    clear_list.append(clear_value)

                else:
                    clear_list.append(item)

            return clear_list
        else: return data


    @staticmethod
    def vspace(text: str) -> str:
        """
        Remove extra spaces from text.

        Args:
        text (str): Input text.

        Returns:
        str: Text with extra spaces removed.
        """
        return ' '.join(text.split())
    
    
    @staticmethod    
    def valpha(text: str) -> str:
        """
        Remove non-alphabetic characters (except a-z, A-Z) from text.

        Args:
        text (str): Input text.

        Returns:
        str: Filtered text containing only alphabetic characters.
        """
        clear_text = ''.join(char for char in text if char.isalpha() or char.isspace())
        return clear_text

    

    @staticmethod    
    def vnum(text: str) -> str:
        """
        Remove non-numeric characters from text.

        Args:
        text (str): Input text.

        Returns:
        str: Filtered text containing only numeric characters.
        """
        clear = ''.join(char for char in text if char.isdigit())
        return clear
    

    @staticmethod
    def vtext(text: str) -> str:
        """
        Remove non-alphanumeric characters (except a-z, A-Z, 0-9) from text.
        Double spaces are replaced with a single space.

        Args:
        text (str): Input text.

        Returns:
        str: Filtered text containing only alphanumeric characters.
        """
        clear_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        
        clear_text = re.sub(r'\s+', ' ', clear_text)
        return clear_text





