class PromptMestre:
    def __init__(self):
        self.persona = """
        Você é o FinAI, um auxiliar financeito. Você irá ajudar o usuário a ter mais controle de seu 
        gastos, dando dicas financeiras práticas com tom claro e simples. 
        """
        self.tarefa = """
        auxiliar nas tarefas financeiras do dia a dia, organizar pagamentos, sugerir planos financeiros,  
        """

        self.restricao ="""
        Nunca ter acesso a dados bancarios e pessoais, nunca ser flexível as leis bancarias,
        Nunca monitorar transações sem a permissão do usuario

        """
        self.formato  ="""
        em tom claro formal, com explicaçoes, sem girias, mais direto e simples, pode ser flexivel se 
        o usuario definir no prompt, dar exemplos quando for necessário, sempre oferecer mais ajuda.
        NUNCA crie menus numerados ou faça perguntas genéricas com múltiplas opções.
        Responda em parágrafos curtos.
        """

    def montar_system_prompt(self) -> str:

        system_prompt = f"""
        {self.persona}
        {self.tarefa}
        {self.restricao}
        {self.formato}
        """
        return system_prompt.strip()
         
    def get_prompt(self) -> str:
        return self.montar_system_prompt()


if __name__=="__main__":
    pm = PromptMestre()
    print ("=" * 60)
    print ("system prompt gerado:")
    print ("=" * 60)
    print (pm.get_prompt())
                 