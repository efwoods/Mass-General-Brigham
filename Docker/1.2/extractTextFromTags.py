import argparse, bs4, requests, re, textwrap

'''
Method: extract
Input:
    url: The url to be parsed
    tags: a list of tags to be parsed from the url; 
    tags are treated as case insensitive, and stripped of '<!/>' characters
Output:
    list_of_extracted_data: 
        A list of strings found within each tag; 
        Contains all text found within tags nested inside the requested tag;
        
        Assumptions:
            If a tag does not contain text within the tag 
                or within any of the tags nested inside of the requested tag,
                the value stored inside the list of extracted data will be ''.
            If a tag is not found in the html document, 
                no content will be added to the list_of_extracted_data for that tag.

'''

def extract(url, tags):
    res = requests.get(url);
    res.raise_for_status();
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #print('Number of tags: {}'.format(len(tags)))
    list_of_extracted_data = []
    for unique_tag_index in range(0,len(tags)):
        #print('tag #{}:'.format(unique_tag_index+1))
        regex_search_string = "^" + tags[unique_tag_index].strip('<!/>') + "$"
        #print('regex search string: {}'.format(regex_search_string))
        unique_tag_list = soup.find_all(re.compile(regex_search_string,re.I))
        #print(unique_tag_list)
        #print('result length: {}'.format(len(unique_tag_list)))
        for tag_data in range(0,len(unique_tag_list)):
            list_of_extracted_data.append(unique_tag_list[tag_data].text);
    #print('list_of_extracted_data: {}'.format(list_of_extracted_data))
    return list_of_extracted_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-u','--url', dest='url', type=str, required=True)
    parser.add_argument('-t','--tags', dest='tags', nargs='+', required=True, 
       help=textwrap.dedent('''\
       Method: extract
Input:
    url: The url to be parsed
    tags: a list of tags to be parsed from the url; 
    tags are treated as case insensitive, and stripped of '<!/>' characters
Output:
    list_of_extracted_data: 
        A list of strings found within each tag; 
        Contains all text found within tags nested inside the requested tag;
        
        Assumptions:
            If a tag does not contain text within the tag 
                or within any of the tags nested inside of the requested tag,
                the value stored inside the list of extracted data will be ''.
            If a tag is not found in the html document, 
                no content will be added to the list_of_extracted_data for that tag.'''))
    args = parser.parse_args()

    result_l = extract(args.url, args.tags);
    print(result_l)

