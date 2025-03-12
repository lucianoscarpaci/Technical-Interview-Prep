# Given a string of HTML-likw tags, write a function to determine if the tags
# are properly nested and closed. The tags will be in the form of <tag>
# for opening tags and </tag> for closing tags. 
def validate_html_tags(html):
  # Create a stack to store the tags
  stack = []
  matches = {
    "<div>": "</div>",
    "<p>": "</p>",
    "<a>": "</a>"
  }
  # Iterate through the html string
  i = 0
  print(len(html))
  while i < len(html):
    # Find the opening tag
    if html[i] == '<':
        # Find the end of the tag
        j = html.find('>', i)
        if j == -1:
            return False # No closing tag found
        # Extract the html tag
        tag = html[i:j+1] #<div>, <p>
        if tag in matches:
            stack.append(tag)
        elif tag in matches.values():
            if not stack or matches[stack[-1]] != tag:
                return False
            stack.pop()
        
        i = j + 1 #correct
    
        if not stack:
            return True



html = "<div><p></p></div>"
print(validate_html_tags(html))

html_2 = "<div><p></div></p>"
print(validate_html_tags(html_2))

html_3 = "<div><p><a></a></p></div>"
print(validate_html_tags(html_3))

html_4 = "<div><p></a></p></div>"
print(validate_html_tags(html_4))
'''
True
False
True
False
'''