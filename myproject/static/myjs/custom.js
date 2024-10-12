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



//End Add to Cart

// Print Table 


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






