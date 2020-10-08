def sq_foot():
    width = int(input("Enter your width ")) #takes users input for width
    length = int(input("Enter your length ")) #takes users input for length
    #may need a clear_output()
    area = length * width
    return (f'Your House\'s Square Footage is equal to {area}ft')
    
sq_foot()