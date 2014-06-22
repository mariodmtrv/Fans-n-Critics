/**
 * Created by mario-dimitrov on 6/22/14.
 */
$(':radio').change(
    function () {
        $('.choice').text(this.value + ' stars');
    }
)