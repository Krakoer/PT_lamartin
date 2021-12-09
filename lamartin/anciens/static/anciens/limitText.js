$(document).ready(function(){
    $('#anciens-table').DataTable(
        {
            "language": {
                "lengthMenu": "_MENU_ anciens par page",
                "zeroRecords": "Pas trouvé déso",
                "info": "page _PAGE_ de _PAGES_",
                "infoEmpty": "Pas de données",
                "infoFiltered": "(sur _MAX_ anciens au total)"
            },
        }
    );
    $('.limit').each(function (f) {
  
        var newstr = $(this).text().substring(0,120)+"...";
        $(this).text(newstr);
  
      });
  })
