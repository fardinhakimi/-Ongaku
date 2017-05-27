
(function(){

/* accordion start */
    $(".accordion").on("click",function(event){
        /* prevent form submission */
        event.preventDefault();
        /* toggle class */
        $(this).toggleClass("active");
        var panel = $(this).parent().next("div");
        panel = panel[0]
        var arrow = $(this).find("i");
        if (panel.style.maxHeight){
            panel.style.maxHeight = null;
            arrow.toggleClass(" glyphicon-plus").removeClass(" glyphicon-minus");
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
            arrow.toggleClass(" glyphicon-minus").removeClass(" glyphicon-plus");

        }
    });


/* date picker */
    $("#id_birth_date" ).datepicker();

})();