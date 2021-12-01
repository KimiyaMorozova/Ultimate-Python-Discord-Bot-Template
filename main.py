
##Imports
import discord
from discord.ext import commands
import STATICS

##Set Up Bot Variables

intents = discord.Intents.all()                                                                 #Use Only when you set up Intents --> https://discord.com/developers/docs/topics/gateway#gateway-intents
prefix = STATICS.Präfix                                                                         #Get the präfix that is definied in the STATICS File
bot = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents)               #remove intents when you don't have any
bot.remove_command('help')                                                                      #Removes the help command if you wish to. Remove when you want to use the default help command.  



#Loading the cogs (command's writing in other files) | cogs.servercogs._example_cog_here for server cogs | cogs.usercogs._example_cog_here for user cogs 
#! Seperate cogs by a ","
startup_extensions = [
    'cogs.system.Logger', 
    'cogs.example_command_cog'
    ]

##Startup defs
def loading(): 
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print(f'{extension} successfully loaded')               #Print if a Cog got succesfully loaded
        except Exception as e:
            exc = f'{type(e).__name__}: \n {e}'                     #Get the Error if there is one while loading a cog and print it to console 
            print(f'Error when loading {extension}\n{exc}')


##Starts The Bot 


@bot.event
async def on_ready(): 
    print ('-----------------')
    print(f'Logging in as {bot.user}')                #Shows the Bot User
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Template made by Kimiya#6974")) #Adds A Status to the Bot
    print("------------------")
    print("Loading Modules...")
    loading()                                         #Calls the Loading Function to load the cogs
    print("Module Load Complete...")
    print('------------------')
    print("Bot complete Online")




bot.run(STATICS.TOKEN)        #! Be sure to add a Token First