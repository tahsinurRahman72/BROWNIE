from brownie import SetIndividual, accounts

def test_deploy():
    #Arrange
    account = accounts[0]
    #Act
    setIndividual = SetIndividual.deploy({"from": account})
    initiate = setIndividual.retrieve()
    expected = 0
    assert initiate == expected
    
    
def test_update_indiv():
    #Arrange
    account = accounts[0]
    setIndividual = SetIndividual.deploy({"from": account})
    #Act
    expected = 1
    setIndividual.commitIndividual(1, 257436, 1567216, 1309780, 1196430, 1824709, 0, {"from": account})
    assert expected == setIndividual.retrieve()