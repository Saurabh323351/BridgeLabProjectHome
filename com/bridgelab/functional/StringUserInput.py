from com.bridgelab.utility.Utility import Utility

utility_obj = Utility()
template = "Hello <<username>>, How are you?"
print("Enter your string")
user_string = utility_obj.get_string()
new_string = utility_obj.replace_str(template, "<<username>>", user_string)
print(new_string)

