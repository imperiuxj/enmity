const Discord = require("discord.js");
const dictionary = require("dictionary-en-us");
const Nspell  = require("nspell");

const token = "";
const guildID = "";
const bot = new Discord.Client();

dictionary((err, dict) => {
  let spell = Nspell(dict);
  
  ["xd", "lol", "jk", "ttyl", "afk", "diy", "imo", "lmao", "lmfao", "skid", "wtf", "wth", "jfc", "omfg", "omg", "jfc", "kys"].forEach(i => {
  	spell.add(i);
  });

  bot.on("message", message => {
      if(message.guild.id != guildID) return;
      if(message.author == bot.user) return;

      let words = message.content.split(" ");
      let incorrect;
      let word;
    
      let done = false;
      words.forEach(i => {
		if (spell.correct(i) == false && done == false) {
         	incorrect = spell.suggest(i)[0];
            message.guild.channels.first().startTyping();
            setTimeout(() => {
                if(incorrect) {
                    message.reply(incorrect + "*".repeat(Math.ceil(Math.random()*2)));
                    message.guild.channels.first().stopTyping();
                }
            }, 3000);
            console.log(message.author.name + " was an idiot and spelt " + word + " wrong. Was corrected to " + incorrect);
            done = true;
		}
    });
  });
});

bot.on("ready", () => {
	console.log("[BOT]: Ready");
});

bot.login(token);
