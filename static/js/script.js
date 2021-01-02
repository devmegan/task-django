$( document ).ready(function() {
    // handle user colour theme choice
    $(".colour-img").click(function(){
        let elId = $(this).attr("id");
        let themeClass = `theme-${elId}`
        $(".page-container").removeClass().addClass("page-container container-fluid").addClass(themeClass);
        $("#newColour").val(elId);
    });
     // hide/show update/delete btns when editing task
    $(".card-input").click(function(){
        $(".update-task-btn").addClass("d-none");
        $(".card-btns").removeClass("d-none");
        $(this).parent().siblings(".card-btns").addClass("d-none");
        $(this).parent().siblings(".update-task-btn").removeClass("d-none");
    })
    // re-show/hide elements when abandoning editing task
    $(".card-input").parent().focusout(function(){
        $(this).parent().siblings(".card-btns").removeClass("d-none");
        $(this).parent().siblings(".update-task-btn").addClass("d-none");
    })
});