***Settings***
Resource    resources/base.robot
***Variables***

${arquivo}=     resources/token/token.txt
${key}=         code.key
${criarkey.key}=        novachave.key


***Test Cases***


teste code and decode
    criar key               ${criarkey.key}
    ${key}=     load key        ${criarkey.key}
    ${bytes_file}=    load file       ${arquivo}
    ${conteudo}     encrypt             ${bytes_file}          ${criarkey.key}
    ${encripted}        escrever_arquivo_encryptado     ${arquivo}      ${conteudo}
    log     ${conteudo}         
    sleep   15
    ${decript}  decrypt     ${arquivo}       ${conteudo}           ${criarkey.key}     
    log      ${decript}

    # teste unitario #

    Should be equal    ${bytes_file}        ${decript}