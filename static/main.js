$("#send").click(function(){
  var para = $('textarea#msg').val();
  $.ajax({
    type : 'POST',
    url : "predict",
    data : {'data':para}
  });
});