#promt style
##Alpaca Promt: Used by meta, llama
### Instruction: <SYSTEM_PROMT>
### Input:  <USER_QUERY>
### Response: \n

##ChatML:openai, gemini uses this style
{
    'role':'system'|'user'|'assistant'
    'content':'string'
    }


##INST Prompting
[INST] What is the time now?[/INST]