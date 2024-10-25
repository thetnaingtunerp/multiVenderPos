console.log('custome js working ....')

//Start Category View 

  $('#categoryview-1').DataTable(
  {
    autoWidth: true,
    "lengthMenu": [
      [16, 32, 64, -1],
      [16, 32, 64, "All"]
    ]
  });

  $('#saleview-2').DataTable(
    {
      autoWidth: true,
      "lengthMenu": [
        [16, 32, 64, -1],
        [16, 32, 64, "All"]
      ],
      "ordering": false,
    }
    // { "targets": [0], "searchable": false, "orderable": false, "visible": true }
  );
 



//   new DataTable('#saleerporttbl', {
//     layout: {
//         topStart: {
//             buttons: ['copy', 'csv', 'excel', 'pdf', 'print']
//         }
//     }
// });

new DataTable('#saleerporttbl', {
  layout: {
      topStart: {
          buttons: ['copy', 'excel', 'pdf', 'colvis']
      }
  }
});



  $("#categorylist").on('click', '.removebtn', function() {
    var currenttr = $(this).closest(".catlisttr");
    var cid = currenttr.find(".cid").html();
    // console.log(cid)
    $.ajax({
      url: `/category/delete/${cid}/`,
      method: "GET",
      data:{cid:cid},
      success: function(data){
        alert('Category Delete from List')
          window.setTimeout(function(){ } ,2000);
                          location.reload();
  
          // window.location.href = '/admin/';
      },
      error:function(){
          alert('having some error contact to developer');
      },
                      
    });//end ajax
  });

//Category Edit
  $(".modal-dialog").on('click', '.updateCat', function() {
    var currenttr = $(this).closest(".editmodal");
    var cid = currenttr.find(".cid").html();
    var cat = currenttr.find("input[name=category]").val();
    // console.log(cat);
    $.ajax({
      url: `/category/edit/${cid}/`,
      method: "GET",
      data:{cid:cid, cat:cat},
      success: function(data){
        alert('Category Edit from List')
          window.setTimeout(function(){ } ,2000);
                          location.reload();
  
          // window.location.href = '/admin/';
      },
      error:function(){
          alert('having some error contact to developer');
      },
                      
    });//end ajax

  });


//End Category View 

//Start Add to Cart
$("#productlist").on('click', '.addtocartbtn', function() {
  var currenttr = $(this).closest(".prolisttr");
  var cid = currenttr.find("input[name=pid]").val();
  var pqty = currenttr.find("input[name=pqty]").val();
  // console.log(cid)
  $.ajax({
    url: `/addtocart/`,
    method: "GET",
    data:{cid:cid, pqty:pqty},
    success: function(data){
      alert('Add to Card')
        window.setTimeout(function(){ } ,2000);
                        location.reload();

        // window.location.href = '/admin/';
    },
    error:function(){
        alert('having some error contact to developer');
    },
                    
  });//end ajax
});

//End Add to Cart

//Customer Change
$("#invcustomername").change(function(){
  var a1=$(this).val();
  var drvcurrenttr = $(this).closest(".drvtbltr");
  // var dvrtblid = drvcurrenttr.find(".dvrtblid").val();
  $.ajax({
  url: "/invcustomername/",
  method: "GET",
  data:{a1:a1},
  success: function(data){
    window.setTimeout(function(){ } ,2000);
    location.reload();

  },
  error:function(){
      alert('Error contact to 09-969255445');
  },
                  
});//end ajax

});//End Hour1


// Print Table 
$("#sbtn").on('click', '.invsavebtn', function() {
  let i = $("input[name=customername]").val();
  console.log(i);
  // printTable();
  $.ajax({
    url: `/invoicesave/`,
    method: "GET",
    data:{i:i},
    success: function(data){
      printTable();
      window.setTimeout(function(){ } ,2000);
                        location.reload();
                        // printTable();
        // window.location.href = '/admin/';
    },
    error:function(){
        alert('having some error contact to developer');
    },
                    
  });//end ajax

});

// function printDiv() {
//   var divToPrint = document.getElementById('table');
//   var htmlToPrint = '' +
//       '<style type="text/css">' +
//           'table td {' +
//       'border:1px solid #dddddd;' +
//       'padding:8px;' +
//       '}' +

//       'table  {' +
//       'border-collapse: collapse;' +
//       'width: 100%;' +
//       '}' +

//       '</style>';
//   htmlToPrint += divToPrint.outerHTML;
//   newWin = window.open("");
//   newWin.document.write(htmlToPrint);
//   newWin.print();
//   newWin.close();
// }




function printTable() {
	var el=document.getElementById("saleview-1");
	el.setAttribute('border', '1');
  el.setAttribute('cellpadding', '10');
  
	newPrint=window.open("");
	newPrint.document.write(el.outerHTML);
	newPrint.print();
	newPrint.close();
}






