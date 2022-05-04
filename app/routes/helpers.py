def validate_cat(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"cat {id} is invalid"}, 400))

    cat = Cat.query.get(id)

    if not cat:
        return abort(make_response({"message": f"cat {id} not found"}, 404))

    # for cat in cats:
    #     cats_response.append(
    #         {"id": cat.id,
    #         "name": cat.name,
    #         "breed": cat.breed,
    #         "personality": cat.personality,
    #         "age": cat.age,
    #         "toe_beans": cat.toe_beans}
    #     )

    return cat
