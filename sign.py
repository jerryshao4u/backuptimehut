import hashlib

#  使用cookies登录 https://blog.csdn.net/weixin_43836098/article/details/89433199

#key source : sign计算方法.
#/events.json?baby_id=567609&v=2&width=700&include_rt=true&timestamp=1570600339&sign=be7906194bb5373fd850ca321987dafd
#/events.json?baby_id=567609&before=1499&v=2&width=700&include_rt=true&timestamp=1570600754&sign=9a8e3f2709c48347ba270ee0ae67b25d

'''
function t(e) {
        for (var t = [], n = e.split(" "), r = 0; r < n.length; r++) {
            var o = n[r]
              , i = parseInt(o, 2)
              , a = String.fromCharCode(i);
            t.push(a)
        }
        return t.join("")
    }
    function n(e) {
        e = unescape(e);
        for (var t = String.fromCharCode(e.charCodeAt(0) - e.length), n = 1; n < e.length; n++)
            t += String.fromCharCode(e.charCodeAt(n) - t.charCodeAt(n - 1));
        return t
    }
    function r() {
        for (var e = "", n = 0; n < 6; n++)
            e += 0 === n || 3 === n || 5 === n ? "1" : "0";
        return t(e)
    }
    function o(e) {
        return n(e.join(r()))
    }
var key = ["Vfbi", "98", "97", "98", "96i", "99", "9Bmh", "93", "98ni", "94", "9Bpnnp", "9F", "96go", "9E", "98bfk"]
console.log(o(key))
'''

t = ["Vfbi", "98", "97", "98", "96i", "99", "9Bmh", "93", "98ni", "94", "9Bpnnp", "9F", "96go", "9E", "98bfk"]
ts = "/events.json?baby_id=567609&v=2&width=700&include_rt=true&timestamp=1570600339"
md5ts = hashlib.md5(ts.encode(encoding='utf-8')).hexdigest()
key = "6027a6b45d762a772b97779f078f2065"
user = "949399"
query = "{}deny bad guy{}{}:::".format(user, key, md5ts)
sign = hashlib.md5(query.encode(encoding='utf-8')).hexdigest()
print(sign)