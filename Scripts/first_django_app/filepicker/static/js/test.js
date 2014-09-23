$(function () {
    $('#btn-open').on('click', function(){
        filepicker.setKey('l5uQ3k7FQ5GoYCHyTdZV')

        filepicker.pick({
            mimetypes: ['image/*', 'text/plain'],
            container: 'window',
            services:['COMPUTER', 'FACEBOOK', 'GMAIL']
          },
          function(InkBlob){
            console.log(JSON.stringify(InkBlob));
          },
          function(FPError){
            console.log(FPError.toString());
          }
        );
    })
})

