
( function () {
    const animation = document.getElementById( "animation" );
    animation.style.right = "75px";
    animation.style.filter = "opacity(0%)";
    animation.style.transition = "0.5s";
    setTimeout( function () {
        animation.style.right = "0px";
        animation.style.filter = "opacity(100%)";
        animation.style.transition = "0.5s";
        setTimeout( function () { animation.style.removeProperty( "filter" ); }, 100 );
    }, 500 );
}
)();

var acc = document.getElementsByClassName( "accordion" );
var i;
for ( i = 0; i < acc.length; i++ )
{
    acc[ i ].addEventListener( "click", function () {
        /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
        this.classList.toggle( "active" );

        /* Toggle between hiding and showing the active panel */
        var panel = this.nextElementSibling;
        if ( panel.style.display === "block" )
        {
            panel.style.display = "none";
        } else
        {
            panel.style.display = "block";
        }
    } );
}

document.addEventListener( 'DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call( document.querySelectorAll( '.navbar-burger' ), 0 );

    // Check if there are any navbar burgers
    if ( $navbarBurgers.length > 0 )
    {

        // Add a click event on each of them
        $navbarBurgers.forEach( el => {
            el.addEventListener( 'click', () => {

                // Get the target from the "data-target" attribute
                const target = el.dataset.target;
                const $target = document.getElementById( target );

                // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
                el.classList.toggle( 'is-active' );
                $target.classList.toggle( 'is-active' );

            } );
        } );
    }

} );

async function Consultar ( event ) {
    let id = event.target.value;
    let paciente = [];
    let alergias = [];

    if ( id.length > 5 )
    {
        var requestOptions = {
            method: 'POST',
            headers: {
                "Content-type": "application/json; charset=UTF-8",
                "Access-Control-Allow-Origin": "*"
            }
        };

        await fetch( "http://127.0.0.1:8000/listar-paciente-matricula/" + id, requestOptions )
            .then( response => { console.log( response ); response.json(); } )
            .then( result => paciente.push( result ) )
            .catch( error => console.log( 'error', error ) );

        await fetch( "http://127.0.0.1:8000/listar-alergias-matricula/" + id, requestOptions )
            .then( response => response.json() )
            .then( result => {
                for ( iten in result )
                {
                    alergias.push( result[ iten ] );
                }
            } )
            .catch( error => console.log( 'error', error ) );

        console.log( paciente );

        let dados = paciente.map( ( iten ) => {
            return (
                `<article class="tile is-child box is-white">` +
                `<p class="title is-4 has-text-info is-size-5">Paciente</p>` +
                `<div class="columns">` +
                `<div class="column pt-1 has-text-left">` +
                `<div class="p-3">` +
                `<div>` +
                `<span class="is-size-6 has-text-weight-bold">Matricula SUS: </span>` +
                `<span class="is-size-6">${ iten.matricula_sus }</span>` +
                `</div>` +
                `<div>` +
                `<span class="is-size-6 has-text-weight-bold">Data de registro: </span>` +
                `<span class="is-size-6">${ iten.data_registro }</span>` +
                `</div>` +
                `<div>` +
                `<span class="is-size-6 has-text-weight-bold">Nome: </span>` +
                `<span class="is-size-6">${ iten.nome }</span>` +
                `</div>` +
                `<div>` +
                `<span class="is-size-6 has-text-weight-bold">Sobrenome: </span>` +
                `<span class="is-size-6">${ iten.sobrenome }</span>` +
                `</div>` +
                `<div>` +
                `<span class="is-size-6 has-text-weight-bold">Data de Nascimento: </span>` +
                `<span class="is-size-6">${ iten.data_nasc }</span>` +
                `</div>` +
                `<div>` +
                `<span class="is-size-6 has-text-weight-bold">Tipo sanguínio: </span>` +
                `<span class="is-size-6">${ iten.tipo_sangue }</span>` +
                `</div>` +
                `<div>` +
                `<span class="is-size-6 has-text-weight-bold">Endereço: </span>` +
                `<span class="is-size-6">${ iten.endereco }</span>` +
                `</div>` +
                `<div>` +
                `<span class="is-size-6 has-text-weight-bold">Complemento:</span>` +
                `<span class="is-size-6">${ iten.complemento }</span>` +
                `</div>` +
                `<div>` +
                `<span class="is-size-6 has-text-weight-bold">Bairro: </span>` +
                `<span class="is-size-6">${ iten.bairro }</span>` +
                `</div>` +
                `<div>` +
                `<span class="is-size-6 has-text-weight-bold">CEP: </span>` +
                `<span class="is-size-6">${ iten.cep }</span>` +
                `</div>` +
                `<div>` +
                `<span class="is-size-6 has-text-weight-bold">Cidade: </span>` +
                `<span class="is-size-6">${ iten.cidade }</span>` +
                `</div>` +
                `<div>` +
                `<span class="is-size-6 has-text-weight-bold">UF: </span>` +
                `<span class="is-size-6">${ iten.uf }</span>` +
                `</div>` +
                `</div>` +
                `</div>` +
                `</div>` +
                `<p class="title is-4 has-text-info is-size-5">Alergias</p>` +
                `<div class="columns">` +
                `<div class="column pt-1 has-text-left">` +
                `<div class="p-3">` +
                `<div id="alergias">` +
                `</div>` +
                `</div>` +
                `</div>` +
                `</article>`
            );
        } );

        let alerg = alergias.map( ( iten ) => {
            return (
                `<div>` +
                `<span class="is-size-6 has-text-danger has-text-weight-bold">${ iten.descricao }</span>` +
                `</div>`
            );
        } );

        document.getElementById( "paciente" ).innerHTML = dados;
        document.getElementById( "alergias" ).innerHTML = alerg;

    }


}
