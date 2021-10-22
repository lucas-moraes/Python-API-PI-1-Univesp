
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

