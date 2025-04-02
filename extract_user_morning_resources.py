# Fn double shift: use when Quickly find any file, action, class,
# symbol, tool window, or setting in PyCharm, in your project,
# and in the current Git repository.


#TODO what data is inputted

## object user_brief_resource ##
# title of resource
# description of resource
# URl
class UserBriefResource:
  # constructor
  resource_type = "Morning Brief"
  def __init__(self):
    self.resource_title = input("resource title: ")
    self.resource_description = input("resource description: ")

user_1_resource = UserBriefResource()
user_2_resource = UserBriefResource()

print(user_1_resource.resource_title)
print(user_2_resource.resource_title)

#TODO what is done with the data

#TODO what is the output
# display on a html page
# install flask work with flask
#INFO typically a web frame is used like flask of django
# to transfer a variable/object value to a html.

