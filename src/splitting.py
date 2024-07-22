import re
class Textsplitter:
    
    def split_by_chunks(self,combined_text,chunks_size):
        chunked=[]
        for i in range(0,len(combined_text),chunks_size):
            chunked.append(combined_text[i : i + chunks_size])

        return chunked


    
    def split_by_line(self,combined_text):
        each_line=[]
        for line in combined_text:
            s = re.split(r'[.?]+', line)
            for sentence in s :
                if sentence.strip(): #empty or not
                    each_line.append(sentence)
        return each_line


    def split_by_word(self,combined_text):
        words=[]
        for line in combined_text:
            s=line.split()
            words.append(s)
        return words 
        

    def split_by_character(self,combined_text,delimiter):

        # Escape the delimiter to handle special characters
        escaped_delimiter = re.escape(delimiter)
        
        # Create regex pattern to split by the delimiter
        pattern = f'{escaped_delimiter}'
        
        all_sentences = []
        
        for line in combined_text:
            # Split the line using the delimiter pattern
            s = re.split(pattern, line)
            
            # Filter out any empty strings from the result
            filtered_s = []
            for sentence in s:
                if sentence.strip():  # Check if the segment is not an empty string
                    filtered_s.append(sentence.strip())
            
            all_sentences.extend(filtered_s)
        
        return all_sentences

    def set_splitter(self, combined_text, splitter_callback, *args, **kwargs):
        result = splitter_callback(combined_text, *args, **kwargs)
        return result
