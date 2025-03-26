# Ass1
 
The project manager: is Abdulrahman-mohamed

How work was distributed: I assigned each team member a specific task so that everyone is actively involved, and the workload is shared almost equally. 
How the team collaborated: Using whatsapp. Also, The project butoon Uploading image.png…

Bonus Tasks:
1- Added Forms in admin.py 

2- I used a  custom method that validation for the form field "title":
    2.1-Retrieves the Title: It gets the submitted title from self.cleaned_data['title'].
    2.2-Checks for Prohibited Content: It verifies if the word "Symbols" is part of the title.
    2.3-Raises an Error if Found: If "Symbols" is found, it raises a ValidationError with a custom message, preventing the form from being valid.
    2.4-Returns the Title: If no error is raised, it returns the cleaned title value for further processing.

3-Added (inlines) edit related objects directly on the same page,multiple options, you can manage those options directly when editing  the poll.

4-Added: overrides the default admin form for the model meanning  include extra validations, custom field widgets, or additional logic for how the model data is presented and saved.

5- Created  a function response_add to display a computed value in the admin list view

6- Added a method to check  response_add exit or not and make it uppercase

7- Added (meta Class) which specifies that the form is associated with the (Poll model)


