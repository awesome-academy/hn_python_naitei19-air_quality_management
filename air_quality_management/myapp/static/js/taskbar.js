$(document).ready(function(){
    $("#btn-cities").click(function(){
        $("#heading-cities").show();
        $("#searchbar").show();
        $("#dataTable").show();
        $("#heading-graph").hide();
    });
    $("#btn-graph-all").click(function(){
        $("#heading-cities").hide();
        $("#searchbar").hide();
        $("#dataTable").hide();
        $("#heading-graph").show();
    });
});