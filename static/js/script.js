function mostrarSenha() {

    const senha = document.getElementById("senha");

    if (senha.type === "password") {
        senha.type = "text";
    } else {
        senha.type = "password";
    }
}

// para buscar os tutoriais 
document.addEventListener("DOMContentLoaded", function () {
    const campoBusca = document.getElementById("buscar-tutorial");
    const tutoriais = document.querySelectorAll(".tutorial-card");
    const mensagemVazia = document.getElementById("nenhum-tutorial");

    // Evita erros em páginas que não possuem a busca de tutoriais
    if (!campoBusca || !mensagemVazia || tutoriais.length === 0) {
        return;
    }

    campoBusca.addEventListener("input", function () {
        const termo = campoBusca.value.toLowerCase().trim();
        let encontrados = 0;

        tutoriais.forEach(function (tutorial) {
            const conteudo = tutorial.textContent.toLowerCase();
            const corresponde = conteudo.includes(termo);

            tutorial.hidden = !corresponde;

            if (corresponde) {
                encontrados++;
            }
        });

        mensagemVazia.hidden = encontrados > 0;
    });
});
