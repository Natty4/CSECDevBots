from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import random
import emoji
import os

# Define your Telegram bot token and chat ID
Token = 'TOKEN'
archive_id = '-ID'
admin_user_id = 'ID'

# Create a Telegram bot instance
bot = telegram.Bot(token=Token)

# Define a set to keep track of users who have generated a name
users_generated_name = set()
print("Bot started")
print('Listening...___________________________________--')

def generate_unique_name(name):
    

    # emojis = ['\U0001F600', '\U0001F601', '\U0001F602', '\U0001F603', '\U0001F604', '\U0001F605', '\U0001F606', '\U0001F607', '\U0001F608', '\U0001F609', '\U0001F60A', '\U0001F60B', '\U0001F60C', '\U0001F60D', '\U0001F60E', '\U0001F60F', '\U0001F610', '\U0001F611', '\U0001F612', '\U0001F613', '\U0001F614', '\U0001F615', '\U0001F616', '\U0001F617', '\U0001F618', '\U0001F619', '\U0001F61A', '\U0001F61B', '\U0001F61C', '\U0001F61D', '\U0001F61E', '\U0001F61F', '\U0001F620', '\U0001F621', '\U0001F622', '\U0001F623', '\U0001F624', '\U0001F625', '\U0001F626', '\U0001F627', '\U0001F628', '\U0001F629', '\U0001F62A', '\U0001F62B', '\U0001F62C', '\U0001F62D', '\U0001F62E', '\U0001F62F']

    adjectives = [
    'Agile🦾', 'Analytical🔍', 'Attentive👀', 'Brilliant🌟', 'Capable💪', 'Collaborative🤝', 'Committed🔒', 'Communicative💬',
    'Competent👌', 'Creative🎨', 'Critical🤔', 'Customerfocused👥', 'Detailoriented🔍', 'Diligent👷', 'Disciplined🕰️',
    'Dynamic🌀', 'Efficient⚡', 'Empathetic💓', 'Enthusiastic🎉', 'Experienced👨‍🎓', 'Focused🎯', 'Forwardthinking🔮',
    'Friendly😊', 'Goaloriented🏆', 'Hardworking💪', 'Helpful🙏', 'Imaginative🤔', 'Independent🧑‍💼', 'Innovative🚀',
    'Insightful🕵️', 'Intelligent🧠', 'Intuitive👀', 'Knowledgeable📚', 'Logical🤓', 'Meticulous🔍', 'Methodical📊',
    'Motivated🏃', 'Multitasking🤹', 'Objective🎯', 'Organized🗂️', 'Passionate💖', 'Patient⏰', 'Persistent🦾',
    'Pragmatic🤝', 'Precise🎯', 'Problem-solving🤔', 'Professional💼', 'Proactive👍', 'Productive🚀', 'Proficient👨‍💻',
    'Punctual⏰', 'Qualityfocused🔍', 'Quickthinking🧠', 'Rational🤔', 'Reliable🔒', 'Resourceful🧰', 'Respectful🤝',
    'Responsible👮', 'Resultsdriven📈', 'Selfmotivated🚀', 'Skilled👨‍💻', 'Strategic🎯', 'Strongwilled💪',
    'Successful🏆', 'Systematic🔍', 'Talented👨‍🎨', 'Teamoriented👥', 'Technicallysavvy💻', 'Thorough🔍',
    'Thoughtful🤔', 'Timely⏰', 'Trustworthy🔒', 'Userfocused👥', 'Versatile🧑‍🎨', 'Visionary🔮', 'Wellorganized🗂️',
    'Wellprepared📝', 'Willing to learn📚', 'Wise🧐', 'Agileminded🤖', 'Autonomous🤖', 'Decisive🤔', 'Effective👊',
    'Efficient⚡', 'Flexible🧘', 'Imaginative🧐', 'Independent🧑‍💼', 'Innovative🚀', 'Productive🚀', 'Responsive👋'
]
    
    # Choose a random emoji
    random_emoji = random.choice(adjectives).lower()
    print(random_emoji)
    
    # Concatenate the random emoji with the name
    unique_name = f"dev_hackathon_z_{random_emoji}_{name.lower()}"
    
    # Check if the file with the same name already exists
    while os.path.exists(f"{unique_name}.txt"):
        # Choose a new random emoji
        random_emoji = random.choice(adjectives).lower()
        unique_name = f"dev_hackathon_z_{random_emoji}_{name.lower()}"
    
    # Return the unique name
    return unique_name



# Define a dictionary to keep track of the user's context
users_context = {}

# Define a set to keep track of users who have generated a name
users_generated_name = set()


# Define the function to handle the '/send_to' command
def send_to(update, context):
    # Check if the user sending the command is the admin
    user_id = str(update.effective_user.id)
    if user_id != admin_user_id:
        context.bot.send_message(chat_id=user_id, text="Sorry, you're not authorized to use this command.")
        return
    
    # Parse the user ID and message from the command arguments
    args = context.args
    if len(args) < 2:
        context.bot.send_message(chat_id=user_id, text="Usage: /send_to user_id message")
        return
    target_user_id = args[0]
    message_text = ' '.join(args[1:])
    
    # Send the message to the target user through the bot
    context.bot.send_message(chat_id=target_user_id, text=message_text)
# Define the handle_message function
def handle_message(update, context):
    # Get the user's information
    user_id = update.effective_user.id
    username = update.effective_user.username
    firstname = update.effective_user.first_name
    photo_url = ''
    
    # Get the user's profile picture
    user_profile_photos = context.bot.getUserProfilePhotos(user_id)

    # Check if the user has at least one profile photo
    if user_profile_photos.total_count > 0:
        # Get the file ID of the first photo
        file_id = user_profile_photos.photos[0][-1].file_id
        # Get the file object of the photo
        photo_file = context.bot.getFile(file_id)
        # Get the URL of the photo
        photo_url = photo_file.file_path

    else:
        # Set a default photo URL if the user does not have a profile picture
        photo_url = 'No profile picture'
        
    # Check if the user has already generated a name
    if user_id in users_generated_name and username in users_context:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"You have already generated a name!\n\nYou can now create a repository on [https://github.com/CSEC-ASTU] CSEC-ASTU GitHub org.\n using this name [ {users_context[username]['unique_name']} ] for the Hackathon.\n if you have face any problem or have any comment please contact @csec_devs")
        # Send the user's information and generated name to the admin
        message = f"New Name Generated:\nUsername: {username}\nFirst Name: {firstname}\n message: {update.message.text}"
        bot.send_message(chat_id=admin_user_id, text=message)
    else:
        try:
            # Get the user's message
            text = update.message.text
            
            # Generate a unique name using the message
            unique_name = generate_unique_name(text)
            
            # Send the unique name back to the user
            context.bot.send_message(chat_id=update.effective_chat.id, text=unique_name)
            
            # Save the user's information and generated name in the dictionary
            users_context[username] = {
                'user_id': user_id,
                'firstname': firstname,
                'photo_url': photo_url,
                'unique_name': unique_name
            }
            
            # Add the user to the set of users who have generated a name
            users_generated_name.add(user_id)
            

            # Send the user's information and generated name to the admin
            message = f"New Name Generated:\nUsername: {username}\nFirst Name: {firstname}\nPhoto URL: {photo_url}\nUser Id: {user_id}\nGenerated Name: {unique_name}"
            bot.send_message(chat_id=admin_user_id, text=message)

            # Send a thank you message tothe user
            context.bot.send_message(chat_id=update.effective_chat.id, text="Thank you for generating a name! \n\nYou can now create a repository on [https://github.com/CSEC-ASTU] GitHub org.using this name [ {users_context[username]['unique_name']} ] for the Hackathon.\n if you have face any problem or have any comment please contact @csec_devs")
        
        except Exception as e:
            # If there is an error, send an error message to the user
            context.bot.send_message(chat_id=update.effective_chat.id, text="Oops🐙, something went wrong! Please try again later.")
            # Print the error message to the console
            print(str(e))
    

# Define a function to handle the "/clear_context" command
def clear_context(update, context):
    # Check if the message is from the admin user
    if str(update.effective_user.id) != admin_user_id:
        message = f"Unauthorized access denied for {update.effective_user.first_name}."
        bot.send_message(chat_id=admin_user_id, text=message)
    else:
        # Get the username from the command
        command_parts = update.message.text.split()
        if len(command_parts) != 2:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Please specify a username to clear the context.")
        else:
            username_to_clear = command_parts[1]
            
            # Check if the username exists in the dictionary
            if username_to_clear not in users_context:
                context.bot.send_message(chat_id=update.effective_chat.id, text=f"{username_to_clear} not found in context.")
            else:
                # Remove the user's information from the dictionary

                del users_context[username_to_clear]
                
                # Send a message to the admin confirming the context has been cleared
                context.bot.send_message(chat_id=admin_user_id, text=f"Context cleared for {username_to_clear}") 

# Define the start function
def start(update, context):
    text = text="Welcome to the CSECDev's Bot! For the Hackathon, kindly enter a name (preferably your first name) to create a distinct GitHub Repository name for the Hackathon."
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

# Define the main function
def main():
    # Set up the bot
    updater = Updater(token=Token, use_context=True)
    dispatcher = updater.dispatcher
    
    # Add the handlers for the commands & messages
    send_to_handler = CommandHandler('send_to', send_to)
    start_handler = CommandHandler('start', start)
    clear_context_handler = CommandHandler('clear_context', clear_context)
    message_handler = MessageHandler(Filters.text, handle_message)
    dispatcher.add_handler(send_to_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(clear_context_handler)
    dispatcher.add_handler(message_handler)
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()