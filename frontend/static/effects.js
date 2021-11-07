
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

