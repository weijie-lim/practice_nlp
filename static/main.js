$("#send").click(function(){
  var para = $('textarea#msg').val();
  alert(para)

  $.ajax({
    type : 'POST',
    url : "{{url_for('prediction')}}",
    contentType: 'application/json;charset=UTF-8',
    data : {'data':para}
  });
});