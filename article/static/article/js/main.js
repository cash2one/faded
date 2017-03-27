$(function(){
    var $modal = $('<div class="modal" id="modal"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title">扫描二维码关注</h4></div><div class="modal-body"></div></div></div></div>');
    $modal.on('hidden.bs.modal', function(){
        $(this).remove();
    });
    $('.social-link#wechat').on('click', function(e){
        e.preventDefault();
        var $this = $(e.currentTarget);
        $modal.find('.modal-body').html('<p style="text-align: center;"><img src="' + $this.attr('href') + '" alt=""></p>')
        $('body').append($modal);
        $modal.modal('show');
    });
});
var _hmt = _hmt || [];
(function() {
    var hm = document.createElement("script");
    hm.src = "https://hm.baidu.com/hm.js?5886b7ce87b59c8dcb688f7f787b8773";
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(hm, s);
})();
