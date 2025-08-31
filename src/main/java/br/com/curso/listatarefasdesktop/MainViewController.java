package br.com.curso.listatarefasdesktop;

import br.com.curso.listatarefasdesktop.model.Tarefa;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.control.cell.CheckBoxTableCell;

public class MainViewController {

    @FXML private TableView<Tarefa> tabelaTarefas;
    @FXML private TableColumn<Tarefa, String> colunaDescricao;
    @FXML private TableColumn<Tarefa, Boolean> colunaConcluida;

    @FXML private TextField campoNovaTarefa;
    @FXML private Button botaoAdicionar;

    private ObservableList<Tarefa> listaTarefas;

    @FXML
    public void initialize() {
        // Inicializa a lista
        listaTarefas = FXCollections.observableArrayList();
        tabelaTarefas.setItems(listaTarefas);

        // Liga as colunas às propriedades da classe Tarefa
        colunaDescricao.setCellValueFactory(cellData -> cellData.getValue().descricaoProperty());
        colunaConcluida.setCellValueFactory(cellData -> cellData.getValue().concluidaProperty());

        // Permite checkbox na coluna "Concluída"
        colunaConcluida.setCellFactory(CheckBoxTableCell.forTableColumn(colunaConcluida));
    }

    @FXML
    private void adicionarTarefa() {
        String texto = campoNovaTarefa.getText().trim();
        if (!texto.isEmpty()) {
            listaTarefas.add(new Tarefa(texto, false));
            campoNovaTarefa.clear();
        }
    }
}
