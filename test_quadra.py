import pytest

from datetime import datetime

from classes.quadra import Quadra_BeachTenis


@pytest.fixture
def quadra_beachtenis():
    return Quadra_BeachTenis(nome_quadra="Quadra 1", min_players=2, max_players=6, drenagem=True, qtd_raquete_locacao=2)


def test_quadra_beachtenis_info(quadra_beachtenis):
    """Verifica se as informações são retornadas corretamente."""
    info = quadra_beachtenis.get_locacao_info()
    assert "Quadra 1" in info
    assert "2" in info
    assert "6" in info


def test_quadra_beachtenis_get_locacao_info():
    """Verifica se as informações retornadas pelo método get_locacao() estão corretas."""
    quadra_beachtenis = Quadra_BeachTenis(nome_quadra='Quadra 1', min_players=2, max_players=6, drenagem=True)
    expected_output = "A quadra de Beach Tênis 'Quadra 1' atende de 2 a 6 participantes."
    assert quadra_beachtenis.get_locacao_info() == expected_output


def test_quadra_beachtenis_drenagem():
    """Verifica se a funcionalidade do método drenagem() está correta."""
    quadra_beachtenis = Quadra_BeachTenis(nome_quadra='Quadra 1', min_players=2, max_players=6, drenagem=True)
    assert quadra_beachtenis.drenagem() == "Quadra 1 possui drenagem."



