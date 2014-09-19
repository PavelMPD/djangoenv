$(function(){
    var MyModel = Backbone.Model.extend({
        defaults: {
            size: 10
        }
    })

    var MyCollection = Backbone.Collection.extend({
        model: MyModel
    })

    var coll = new MyCollection()

    var car = new MyModel({
        size: 75
    })

    coll.add(car)
    coll.add({})
    console.log(coll.toJSON())
    coll.remove(car)
    console.log(coll.toJSON())
})