(function () {
    var myConnector = tableau.makeConnector();

    myConnector.getSchema = function (schemaCallback) {
        var cols = [{
            id: "id",
            alias: "ID",
            dataType: tableau.dataTypeEnum.int
        }, {
            id: "year",
            alias: "Year",
            dataType: tableau.dataTypeEnum.int
        }, {
            id: "month",
            alias: "Month",
            dataType: tableau.dataTypeEnum.int
        }, {
            id: "ie_code",
            alias: "IE Code",
            dataType: tableau.dataTypeEnum.int
        }, {
            id: "coa_code",
            alias: "COA Code",
            dataType: tableau.dataTypeEnum.int
        }, {
            id: "coa_name",
            alias: "COA Name",
            dataType: tableau.dataTypeEnum.string
        }, {
            id: "ccc_code",
            alias: "CCC Code",
            dataType: tableau.dataTypeEnum.int
        }, {
            id: "ccc_name",
            alias: "CCC Name",
            dataType: tableau.dataTypeEnum.string
        }, {
            id: "country_code",
            alias: "Country Code",
            dataType: tableau.dataTypeEnum.int
        }, {
            id: "country_name",
            alias: "Country Name",
            dataType: tableau.dataTypeEnum.string
        }, {
            id: "weight",
            alias: "Weight",
            dataType: tableau.dataTypeEnum.int
        }, {
            id: "usd",
            alias: "USD",
            dataType: tableau.dataTypeEnum.int
        }, {
            id: "twd",
            alias: "TWD",
            dataType: tableau.dataTypeEnum.int
        }];

        var tableSchema = {
            id: "tradeTest",
            alias: "Trade for test",
            columns: cols
        };

        schemaCallback([tableSchema]);
    };

    myConnector.getData = function (table, doneCallback) {
        $.ajax({
            beforeSend: function(request) {
                request.setRequestHeader('Authorization', 'Token e65ba8165e86ac541c7f2a2dbf21690599c29cd0');
            },
            dataType: 'json',
            url: '/api/trade/',
            success: function(resp) {
                tableData = [];
            	$.each(resp['results'], function(key, value) {
            		subData = {};
            		$.each(resp['results'][key], function(key2, value2){
            			subData[key2] = value2;
            		})
            		tableData.push(subData);
            	});
                table.appendRows(tableData);
                doneCallback();
            }
        });
    };

    tableau.registerConnector(myConnector);

    // Create event listeners for when the user submits the form
    $(document).ready(function() {
        $("#submitButton").click(function() {
            tableau.connectionName = "Trade"; // This will be the data source name in Tableau
            tableau.submit(); // This sends the connector object to Tableau
        });
    });
})();
