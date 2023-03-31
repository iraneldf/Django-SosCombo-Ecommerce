(function ($) {

    $.fn.filterTable = function (id) {

        if (!id) {
            console.error('You must provide filter input ID in options!');
            return null;
        }

        // var settings = $.extend({
        //   // These are the defaults.
        //   id: ''
        // }, options );
        let bool;
        var filterID = id;
        var table = $(".ubicaciones");

        $(filterID).on("keyup", function () {

            var value = $(this).val().toUpperCase();

            table.find('.provincia-ubicacion').each(function (index) {
                $row = $(this);
                $row.find(".nombre").each(function () {
                    $cell = $(this).text().toUpperCase();


                    if ($cell.indexOf(value) > -1) {
                        bool = true;
                    } else {
                        bool = false;
                    }

                });


                if (bool) {
                    $row.show();
                } else {
                    $row.hide();
                }
            }); // table each

        }); // search keyup

        return this;
    }

})(jQuery)

//
// (function ($) {
//
//     $.fn.filterTable = function (id) {
//
//         if (!id) {
//             console.error('You must provide filter input ID in options!');
//             return null;
//         }
//
//         // var settings = $.extend({
//         //   // These are the defaults.
//         //   id: ''
//         // }, options );
//         let bool;
//         var filterID = id;
//         var table = $(".caja-productos");
//         console.log(table);
//         $(filterID).on("keyup", function () {
//             console.log("funciona");
//             var value = $(this).val().toUpperCase();
//
//             table.find('.plantilla-producto').each(function (index) {
//                 $row = $(this);
//                 $row.find(".nombre").each(function () {
//                     $cell = $(this).text().toUpperCase();
//                     console.log($cell,'CELL');
//
//                     if ($cell.indexOf(value) > -1) {
//                         bool = true;
//                     }else {
//                         bool = false;
//                     }
//                     console.log(bool,"BOOL");
//                 });
//
//
//                 if (bool) {
//                     $row.show();
//                 } else {
//                     $row.hide();
//                 }
//             }); // table each
//
//         }); // search keyup
//
//         return this;
//     }
//
// })(jQuery)