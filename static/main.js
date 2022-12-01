$("#send").click(function(){
  var para = $('textarea#msg').val();
  $.ajax({
    type : 'POST',
    url : "predict",
    data : {'data':para},
  }).then(
    function (response) {
      var response = JSON.parse(response);
      $('#category').html("Category: " + response['prediction']);
      $('#probability').html("Probability: " + response[response['prediction']]);
      $('#amendments').html(response['amendments']);
      $('#counterparts').html(response['counterparts']);
      $('#laws').html(response['governing laws']);
      $('#reg').html(response['government regulations']);
      $('#terminations').html(response['terminations']);
      $('#trade_relations').html(response['trade relations']);
      $('#trading_activities').html(response['trading activities']);
      $('#valid_issuances').html(response['valid issuances']);
      $('#waivers').html(response['waivers']);
      $('#warranties').html(response['warranties']);
      console.log(response)
    }
  );
});