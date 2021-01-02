$( document ).ready(function() {
    // handle user colour theme choice
    $(".colour-img").click(function(){
        let elId = $(this).attr("id");
        let themeClass = `theme-${elId}`
        $(".page-container").removeClass().addClass("page-container container-fluid").addClass(themeClass);
        $("#newColour").val(elId);
    });
});