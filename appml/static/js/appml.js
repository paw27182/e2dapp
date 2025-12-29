/*-----------------------------------
 appml/static/html/
  inquire_appml.html - #btn_execute
-----------------------------------*/
$(function () {
    $('#btn_execute').off().on("click", function () {

        $("#area4Result").empty();  // clear result area

        var command = $("#selected_dropdown_item").val();  // Submit_a_form or Get a list of forms ...
        console.log("[appml.js] command= ", command);

        // formData for POST
        var formData = new FormData($('#uploadForm')[0]);  // FormData object
        formData.append("command", command);

        // deactivate button
        $('#btn_execute').prop("disabled", true);
        $('#btn_execute').text("Executing...");

        $.ajax({
            url: '/appml',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
        })
            .done(function (output, status, xhr) {
                // console.log(xhr.getResponseHeader("Content-Type"));
                // console.log(xhr.getResponseHeader("Results"));
                // console.log(output)

                $('#area4Result').html(output);
                $('#area4Result').show();

                // activate button
                $('#btn_execute').prop("disabled", false);
                $('#btn_execute').text("Execute");

            })
            .fail(function (error) {
                console.log(error);
            });  // ajax
    });  // function
});  // function


/*----------------------------------------
 appml/templates/appml/
   area4Inquire_appml.html - .btn_result
----------------------------------------*/
$(function () {
    $('.btn_result').off().on("click", function () {

        $("#area4Result").empty();  // clear result area

        var command = $(this).attr("id");
        console.log("[appml.js] command= ", command);

        var selected_form = $(this).attr("value1");
        console.log("[appml.js] selected_form= ", selected_form);

        var groupname = $(this).attr("value2");
        console.log("[appml.js] groupname= ", groupname);

        // formData for POST
        var formData = new FormData($('#uploadForm')[0]);  //FormData object
        formData.append("command", command);
        formData.append("selected_form", selected_form);
        formData.append("groupname", groupname);

        // deactivate button
        $('#btn_execute').prop("disabled", true);
        $('#btn_execute').text("Executing...");

        $.ajax({
            url: '/appml',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
        })
            .done(function (output, status, xhr) {
                // console.log(xhr.getResponseHeader("Content-Type"));
                // console.log(xhr.getResponseHeader("Results"));
                // console.log(output)

                $('#area4Result').html(output);
                $('#area4Result').show();

                // activate button
                $('#btn_execute').prop("disabled", false);
                $('#btn_execute').text("Execute");

            })
            .fail(function (error) {
                console.log(error);
            });  // ajax
    });  // function
});  // function


///*-------------------------------------------------------------  2023.6.20
//  templates/appml/area4Parameters_appml.html - .btn_execute_mls
//--------------------------------------------------------------*/
//$(function(){
//	$('.btn_execute_mls').off().on("click", function(){
//
//        $("#area4Result").empty();  // clear result area
//
//        var command = $(this).attr("value0");
//        var selected_form = $(this).attr("value1");
////        var database_type = $(this).attr("value2");
//        var groupname = $(this).attr("value2");  // 2022.2.22
//        var executeParameters = $(this).attr("value3");  // 2022.2.22
//
//        // formData for POST
//        var formData = new FormData($('#uploadForm')[0]);  //FormData object
//        formData.append("command", command);
//        formData.append("selected_form", selected_form);
//        formData.append("groupname", groupname);
//        formData.append("executeParameters", executeParameters);
//
//        // deactivate button
//        $('.btn_execute').prop("disabled", true);  // NOT .btn_execute_mls
//        $('.btn_execute').text("Executing...");  // NOT .btn_execute_mls
//
//		$.ajax({
//			url: '/appml',  // 2022.3.29
//			type: 'POST',
//			data: formData,
//            processData: false,  // 2020.8.14
//            contentType: false,  // 2020.8.14
//            })
//			.done(function(output, status, xhr){
////				console.log(xhr.getResponseHeader("Content-Type"));
////				console.log(xhr.getResponseHeader("Results"));
////				console.log(output)
//
//                $('#area4Result').html(output);
//                $('#area4Result').show();
//
//				// activate button
//			    $('.btn_execute').prop("disabled", false);
//			    $('.btn_execute').text("Execute");
//
//			})
//			.fail(function(error){
//				console.log(error);
//			});  // ajax
//	});  // function
//});  // function
