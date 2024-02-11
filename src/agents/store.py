from messages.store import Search, PlaceOrder

from messages.customer import SearchResult

from uagents import Agent, Context



agent = Agent(name='store')

jls_extract_var = 'smartwatches3'
product_data = {
    'laptops': {

        'Laptop1': {'price': 1000, 'availability': True},

        'Laptop2': {'price': 1200, 'availability': False},

        'Laptop3': {'price': 800, 'availability': True}
    },
    

    'tv': {

        'TV1': {'price': 500, 'availability': True},

        'TV2': {'price': 700, 'availability': True},

        'TV3': {'price': 1000, 'availability': False}
    },
    

    'smartphones': {

        'Phone1': {'price': 300, 'availability': True},

        'Phone2': {'price': 400, 'availability': True},

        'Phone3': {'price': 600, 'availability': False}
    },
    

    'watches': {

        'Watch1': {'price': 100, 'availability': True} ,

        'Watch2': {'price': 150, 'availability': False},

        'Watch3': {'price': 120, 'availability': True}
    },


    'smartwatches': {

        'smartwatches1': {'price': 1000, 'availability': False},

        'smartwatches2': {'price': 1199, 'availability': True},
        
        'smartwatches3': {'price': 1499, 'availability': True}
    },


    'electric heaters': {

            'electric heater1': {'price': 999, 'availability': False},

            'electric heater2': {'price': 699, 'availability': True},

            'electric heater3': {'price': 1499, 'availability': True}
    },


    'washing machines': {

            'washing machine1': {'price': 15990, 'availability': False},

            'washing machine2': {'price': 8000, 'availability': True},

            'washing machine3': {'price': 6990, 'availability': False}
    },


    'refrigerators': {

            'refrigerator1': {'price': 15990, 'availability': False},

            'refrigerator2': {'price': 3050, 'availability': True},

            'refrigerator3': {'price': 6990, 'availability': True}
    },

    'computers': {

            'computer1': {'price': 15000, 'availability': True},

            'computer2': {'price': 25000, 'availability': True},

            'computer3': {'price': 13000, 'availability': True}
    }
}

@agent.on_message(model=Search)

async def handel_search(ctx: Context, sender: str, msg: Search):

    data = []

    for i in product_data:

        if msg.item_name in i.lower() or i.lower() in msg.item_name:
            

            if msg.max_price == msg.min_price:

                data.append(product_data[i])

            else:

                new_data = {}

                for k in product_data[i]:

                    if msg.max_price >= product_data[i][k]['price'] and msg.min_price <= product_data[i][k]['price']:

                        new_data[k] = product_data[i][k]


                data.append(new_data)
                

    if data:

        await ctx.send(sender, SearchResult(result=data))
    else:

        ctx.logger.info(f'We dont sell this type of product')



@agent.on_message(model=PlaceOrder)

async def place_order(ctx, sender, msg):

    data = msg.item

    for i in data:

        ctx.logger.info(f"You have ordered {i} of cost {data[i]['price']}")


    ctx.logger.info("Order Placed Successfully\n\n\n\n\n")
    



